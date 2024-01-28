#include <kernel.h>
#include "kernel_cfg.h"
#include "app.h"

#include "mbed.h"

#include "app_config.h"

#include "Zumo.h"
#include "Milkcocoa.h"

Serial pc(USBTX, USBRX);
Zumo zumo;

#include "GR_PEACH_WlanBP3595.h" // Added
GR_PEACH_WlanBP3595 wlan;		 // Added
IrBitField_T irbits;
short ax, ay, az;

#define PRIVATE 0 // 自家用車：クライアント
#define RESCUE 1  // 救助車：サーバ

// 今の状態
// 0:初期化
// 1:移動中(自)
// 2:待機中(救)
// 3:待機中(自)
// 4:移動中(救)
// 5:救助中(自)
// 6:救助中(救)
// 6:反転＋帰還中yy
// 7:終了

static int current_status;
const int CAR_ROLE = RESCUE; // CHANGE HERE FOR ROLE

// LINE TRACE
void line_trace(void); // main
void left_weak(void);
void left_normal(void);
void left_strong(void);
void right_weak(void);
void right_normal(void);
void right_strong(void);
void stop(void);
void reversal(void);

void task_main(intptr_t exinf)
{
	// ===== 0. INIT =====
	// 0-1. Init start
	current_status = 0;
	// 0-2. Debug
	pc.baud(9600);
	// 0-2. Sensor
	// IrBitField_T irbits; // Gravitational sensor
	// 0-3. Wi-Fi
	const char *WIFISSID = "CLab";
	const char *WIFIPASSWORD = "TeamCollaboration";
	const char *MYADDRESS;
	const char *SERVERADDRESS;
	const char *MASK = "255.255.255.0";
	const char *GATEWAY = "192.168.11.1";
	const int PORT = 5000;
	int TIME = 1500;
	char buffer[128];
	char *Message = "Hello";
	if (CAR_ROLE == PRIVATE)
	{
		SERVERADDRESS = "192.168.11.101"; // Required only for clients
		MYADDRESS = "192.168.11.102";	  // 1. Client IP
	}
	else if (CAR_ROLE == RESCUE)
		MYADDRESS = "192.168.11.101"; // 2. Server IP
	wlan.init(MYADDRESS, MASK, GATEWAY);
	if (wlan.connect(WIFISSID, WIFIPASSWORD) == 0)
		pc.printf("Connected to the network.\r\n");
	pc.printf("Connection phase finished.\r\n");
	// 0-4. TCP
	TCPSocketConnection client;
	TCPSocketServer server;
	if (CAR_ROLE == PRIVATE)
	{
		// client.connect(SERVERADDRESS, PORT);    // Connect to the server
		if (client.connect(SERVERADDRESS, PORT))
			pc.printf("Connected to the rescue car.\r\n");
	}
	else if (CAR_ROLE == RESCUE)
	{
		server.bind(PORT); // Bind the server to the defined port
		server.listen();   // Listen for connections
		if (server.accept(client) == 0)
			pc.printf("Connected to the private car.\r\n");
		else
			pc.printf("Connection failed.\r\n");
		client.set_blocking(false, TIME); // Set the timeout time
	}
	pc.printf("Init phase ended.\r\n");
	zumo.buzzerOn();
	dly_tsk(1000);
	zumo.buzzerOff();
	// init end

	// ===== 1. WAIT_S =====
	if (CAR_ROLE == RESCUE)
	{
		current_status = 1;
		while (true)
		{
			// if received message from client, break
			if (client.receive(buffer, 5) > 0)
			{
				pc.printf("Message received; Going to rescue.\r\n");
				zumo.buzzerOn();
				dly_tsk(1000);
				zumo.buzzerOff();
				break;
			}
			else{
				pc.printf("Message not received; Going to rescue.\r\n");
				dly_tsk(1000);
			}
		}
		current_status = 4;
		// go to rescue
		// if arrived & stopped, send message to client
		line_trace();
		if (client.send(Message, strlen(Message)) > 0)
		{
			pc.printf("Message sent; Car rescued.\r\n");
			zumo.buzzerOn();
			dly_tsk(1000);
			zumo.buzzerOff();
		}
		else{
			pc.printf("Message not sent; Car not rescued.\r\n");
			dly_tsk(1000);
		}
	}

	// ===== 2. MOVE_C =====
	if (CAR_ROLE == PRIVATE)
	{
		current_status = 2;
		// linetrace. if accident happened, send message to server and break
		line_trace();
		zumo.setBuzzerHz(600);
		zumo.buzzerOn();
		dly_tsk(500);
		zumo.buzzerOff();

		while (true)
		{
			if (client.send(Message, strlen(Message)) > 0)
			{
				pc.printf("Message sent; Accident happened.\r\n");
				zumo.buzzerOn();
				dly_tsk(1000);
				zumo.buzzerOff();
				break;
			}
			else{
				pc.printf("Message not sent; Accident happened.\r\n");
				dly_tsk(1000);
			}
		}
		current_status = 3;
		while (true)
		{
			if (client.receive(buffer, 5) > 0)
			{
				pc.printf("Message received; Rescue successful.\r\n");
				zumo.buzzerOn();
				dly_tsk(1000);
				zumo.buzzerOff();
				break;
			}
			else{
				pc.printf("Message not received; Rescue failed.\r\n");
				dly_tsk(1000);
			}
		}
		// wait for response
		// if received message from server, break
	}

	// ===== 3. WAIT_C =====
	/*if (CAR_ROLE == PRIVATE)
	{
		current_status = 3;
		while (true)
		{
			if (client.receive(buffer, 5) > 0)
			{
				pc.printf("Message received; Rescue successful.\r\n");
				zumo.buzzerOn();
				dly_tsk(1000);
				zumo.buzzerOff();
				break;
			}
			else{
				pc.printf("Message not received; Rescue failed.\r\n");
				dly_tsk(1000);
			}
		}
		// wait for response
		// if received message from server, break
	}*/

	// ===== 4. MOVE_S =====
	/*if (CAR_ROLE == RESCUE)
	{
		current_status = 4;
		// go to rescue
		// if arrived & stopped, send message to client
		line_trace();
		if (client.send(Message, strlen(Message)) > 0)
		{
			pc.printf("Message sent; Car rescued.\r\n");
			zumo.buzzerOn();
			dly_tsk(1000);
			zumo.buzzerOff();
		}
		else{
			pc.printf("Message not sent; Car not rescued.\r\n");
			dly_tsk(1000);
		}
	}*/

	// ===== 5. RETURN =====
	current_status = 7;
	dly_tsk(1000);
	reversal();
	line_trace();
	// wait for 1 sec, reverse, return, and end
}


// USER-DEFINED FUNCTIONS
void left_weak(){
	zumo.driveTank(60,250);
}
void left_normal(){
	zumo.driveTank(0,220);
}
void reversal(){
	IrBitField_T irbits;
	zumo.driveTank(-100,100);
	dly_tsk(1000);
	while(true){
		zumo.readIr(irbits);
		if(irbits.right){
				break;
			}
	}
	zumo.driveTank(0,0);
}
void stop(){
	zumo.driveTank(0,0);
}

void right_weak(){
	zumo.driveTank(250,100);
}

void right_normal(){
	zumo.driveTank(220,0);
}



//left_strongは急角度に対応するために作成
void left_strong(){
	IrBitField_T irbits;
		zumo.driveTank(-200,225);//左旋回だが、旋回のみだと太線でturn_rightと繰り返し実行してしまうため、進みながら旋回している
		while(true){
			zumo.getAcceleration(&ax,&ay,&az);
								  zumo.readIr(irbits);
								  if(ax<-10000 && (ay<-4000 || ay>4000)){
									  break; //加速度センサで抜け出してとまる
								  }
			zumo.readIr(irbits);
			if(irbits.right){
					break;//右のセンサが黒を感知するまで旋回を行う
				}
		}
		zumo.readIr(irbits);
		//このif文は急角度の対応だけでなく、太線に対応するために作成
		//(0,1,1)の時if文に突入
		if(irbits.center && irbits.right){
			//このwhile文は(1,1,1)か(0,1,0)でぬけだす
			while(true){
				zumo.getAcceleration(&ax,&ay,&az);
									  zumo.readIr(irbits);
									  if(ax<-10000 && (ay<-4000 || ay>4000)){
										  break; //加速度センサで抜け出してとまる
									  }
				zumo.readIr(irbits);
				if(irbits.center && irbits.right && irbits.left){
					stop();//(1,1,1)でとまって抜け出す
					break;
				}
				else if(irbits.center && irbits.right){
					zumo.driveTank(250,191);//(0,1,1)で弱く右
				}
				else if(irbits.center && irbits.left){
					zumo.driveTank(191,250);//(1,1,0)で弱く左
				}
				else if(irbits.center){
					break;//(0,1,0)で抜け出す(太線を抜け出したと判定したため)
				}
				else if(irbits.right){
					zumo.driveTank(220,0);//(0,0,1)の場合(0,1,0)になるまで右に進みながら旋回
					while(true){
						zumo.getAcceleration(&ax,&ay,&az);
											  zumo.readIr(irbits);
											  if(ax<-10000 && (ay<-4000 || ay>4000)){
												  break; //加速度センサで抜け出してとまる
											  }
						zumo.readIr(irbits);
						if(irbits.center){
							break;
						}
					}
				}
				else if(irbits.left){
					zumo.driveTank(0,220);//(1,0,0)の場合(0,1,0)になるまで左に進みながら旋回
					while(true){
						zumo.getAcceleration(&ax,&ay,&az);
											  zumo.readIr(irbits);
											  if(ax<-10000 && (ay<-4000 || ay>4000)){
												  break; //加速度センサで抜け出してとまる
											  }
						zumo.readIr(irbits);
						if(irbits.center){
							break;
						}
					}
				}
				}
		}
}

//right_strongは急角度に対応するために作成
void right_strong(){
	IrBitField_T irbits;
		zumo.driveTank(225,-200);//右旋回だが、旋回のみだと太線でturn_leftと繰り返し実行してしまうため、進みながら旋回している
		while(true){
			zumo.getAcceleration(&ax,&ay,&az);
					  zumo.readIr(irbits);
					  if(ax<-10000 && (ay<-4000 || ay>4000)){
						  break; //加速度センサで抜け出してとまる
					  }
			zumo.readIr(irbits);
			if(irbits.left){
					break;//左のセンサが黒を感知するまで旋回を行う
				}
		}
		zumo.readIr(irbits);
		//このif文は急角度の対応だけでなく、太線に対応するために作成
		if(irbits.center && irbits.left){
			        //このwhile文は(1,1,1)か(0,1,0)でぬけだす
					while(true){
						zumo.getAcceleration(&ax,&ay,&az);
											  zumo.readIr(irbits);
											  if(ax<-10000 && (ay<-4000 || ay>4000)){
												  break; //加速度センサで抜け出してとまる
											  }
						zumo.readIr(irbits);
						if(irbits.center && irbits.right && irbits.left){
							stop();//(1,1,1)でとまって抜け出す
							break;
						}
						else if(irbits.center && irbits.left){
							zumo.driveTank(191,250);//(1,1,0)で弱く左
						}
						else if(irbits.center && irbits.right){
							zumo.driveTank(250,191);//(0,1,1)で弱く右
						}
						else if(irbits.center){
							break;//(0,1,0)で抜け出す(太線を抜け出したと判定したため)
						}
						else if(irbits.right){
							zumo.driveTank(220,0);//(0,0,1)の場合(0,1,0)になるまで右に進めながら旋回
							while(true){
								zumo.getAcceleration(&ax,&ay,&az);
													  zumo.readIr(irbits);
													  if(ax<-10000 && (ay<-4000 || ay>4000)){
														  break; //加速度センサで抜け出してとまる
													  }
								zumo.readIr(irbits);
								if(irbits.center){
									break;
								}
							}
						}
						else if(irbits.left){//(1,0,0)の場合(0,1,0)になるまで左に進めながら旋回
							zumo.driveTank(0,220);
							while(true){
								zumo.getAcceleration(&ax,&ay,&az);
													  zumo.readIr(irbits);
													  if(ax<-10000 && (ay<-4000 || ay>4000)){
														  break; //加速度センサで抜け出してとまる
													  }
								zumo.readIr(irbits);
								if(irbits.center){
									break;
								}
							}
						}
					}
				}
}

void line_trace(){
	IrBitField_T irbits;
	short ax ,ay ,az;

	while(true){
		zumo.getAcceleration(&ax,&ay,&az);
		  zumo.readIr(irbits);
		  if(ax<-10000 && (ay<-4000 || ay>4000)){
			  break; //加速度センサで抜け出してとまる
		  }else if (irbits.center && irbits.right && irbits.left){
		  		  break;//(1,1,1)で抜け出してとまる

		  } else if(irbits.center == 0 && irbits.left == 0 && irbits.right == 0){
			  right_weak();//(0,0,0)で弱く右
		  }
		  else if(irbits.center && irbits.right){
			  right_strong();//(0,1,1)で右旋回
		  }
		  else if(irbits.center && irbits.left){
			  left_strong();//(1,1,0)で左旋回

		  }
		  else if (irbits.center){
			  left_weak();//(0,1,0)で弱く左

		  } else if (irbits.right){
			  right_normal();//(0,0,1)でみぎ

		  } else if (irbits.left){
			  left_normal();//(1,0,0)で左

		  }
	  }
	  stop();//止まる
}
