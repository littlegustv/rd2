var redis = require('redis');
var shortid = require('shortid');

function TelnetConnection(socket) {
	this.socket = socket;
	this.id = shortid.generate();

	this.pub = redis.createClient();
	this.sub = redis.createClient();
	this.sub.socket = socket;

	this.inputChannel = 'from client ' + this.id;

	this.sub.subscribe('from server ' + this.id);

	this.sub.on('message', function(channel, message) {
		// console.log('in TC sub.on');
		// console.log(this.socket);
		// console.log(message);
		this.socket.write(message + '\r\n');
	})
}

TelnetConnection.prototype.sendInput = function(data) {
	this.pub.publish(this.inputChannel, data);
}

module.exports = TelnetConnection;