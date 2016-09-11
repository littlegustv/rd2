var redis = require('redis');
var net = require('net');
var TelnetConnection = require('./telnetconnection.js');

var pub = redis.createClient();

var connections = [];

var server = net.createServer(
	function (socket) {
		var conn = new TelnetConnection(socket);
		connections.push(conn);

		pub.publish('register', conn.id);

		socket.on('data', function (data) {
			if(data == 'exit') {
				process.exit();
			}
			conn.sendInput(data);
		});

		socket.write('Welcome to Telnet server!');
	}
).listen(4000);
