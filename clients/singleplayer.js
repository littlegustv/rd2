var redis = require('redis');
var shortid = require('shortid');

var sub = redis.createClient();
var pub = redis.createClient();

var id = shortid.generate();

sub.subscribe('from server ' + id);

function getInput() {
	process.stdin.resume();
	process.stdin.setEncoding('utf8');

	process.stdin.on('data', function (text) {
		processedText = text.replace(/\n$/, '')
		pub.publish('from client ' + id, processedText);
	});
}

sub.on('message', function (channel, message) {
	console.log(message);
});

function onErr(err) {
	console.log(err);
	return 1;
}

// Execute main code
if(require.main == module) {
	pub.publish('register', id);

	getInput();
}
