//	Customization

var appPort = 8090;
var fs = require('fs');
// Librairies

var express = require('express'), app = express();
var http = require('http')
  , server = http.createServer(app)
  , io = require('socket.io').listen(server);


var jade = require('jade');
// var io = require('socket.io').listen(app);
var pseudoArray = ['admin']; //block the admin username (you can disable it)


//tcp client

var net = require('net');
var client = new net.Socket();
client.connect(5010, '192.168.1.12', function() {
	console.log('Connected');
	client.write('Hello, server! Love, Client.');
});
 
client.on('data', function(data) {
	console.log('Received: ' + data);
	client.destroy(); // kill client after server's response
});
 
client.on('close', function() {
	console.log('Connection closed');
});



/////////////////
// Views Options

app.set('views', __dirname + '/views');
app.set('view engine', 'jade');
app.set("view options", { layout: false })

app.configure(function() {
	app.use(express.static(__dirname + '/public'));
});

// Render and send the main page

app.get('/', function(req, res){
  res.render('home.jade');
});
server.listen(appPort);
// app.listen(appPort);
console.log("Server listening on port "+appPort );

// Handle the socket.io connections

var users = 0; //count the users

io.sockets.on('connection', function (socket) { // First connection
	users += 1; // Add 1 to the count
	reloadUsers(); // Send the count to all the users
	socket.on('message', function (data) { // Broadcast the message to all
		if(pseudoSet(socket))
		{
			var transmit = {date : new Date().toISOString(), pseudo : returnPseudo(socket), message : data};
			socket.broadcast.emit('message', transmit);
			console.log("user "+ transmit['pseudo'] +" said \""+data+"\"");
									
									fs.appendFile("test.txt",transmit['date'] + " : user "+ transmit['pseudo'] +" said \""+data+"\" \r\n", function(err) {
										if(err) {
												console.log(err);
										} else {
												console.log("The file was saved!");
										}
									}); 
									
									if(data == "ibot"){
										//do something
										client.write('i');
										}
									if(data == "iBot go left"){
										//do something
										client.write('R');
										}
									if(data == "iBot go right"){
										//do something
										client.write('L');
										}
									if(data == "iBot go forward"){
										//do something
										client.write('B');
										}
									if(data == "iBot go backward"){
										//do something
										client.write('F');
										}
									if(data == "iBot go stop"){
										//do something
										client.write('H');
										}

		}
	});
	socket.on('setPseudo', function (data) { // Assign a name to the user
		if (pseudoArray.indexOf(data) == -1) // Test if the name is already taken
		{
			socket.set('pseudo', data, function(){
				pseudoArray.push(data);
				socket.emit('pseudoStatus', 'ok');
				console.log("user " + data + " connected");
			});
		}
		else
		{
			socket.emit('pseudoStatus', 'error') // Send the error
		}
	});
	socket.on('disconnect', function () { // Disconnection of the client
		users -= 1;
		reloadUsers();
		if (pseudoSet(socket))
		{
			var pseudo;
			socket.get('pseudo', function(err, name) {
				pseudo = name;
			});
			var index = pseudoArray.indexOf(pseudo);
			pseudo.slice(index - 1, 1);
		}
	});
});

function reloadUsers() { // Send the count of the users to all
	io.sockets.emit('nbUsers', {"nb": users});
}
function pseudoSet(socket) { // Test if the user has a name
	var test;
	socket.get('pseudo', function(err, name) {
		if (name == null ) test = false;
		else test = true;
	});
	return test;
}
function returnPseudo(socket) { // Return the name of the user
	var pseudo;
	socket.get('pseudo', function(err, name) {
		if (name == null ) pseudo = false;
		else pseudo = name;
	});
	return pseudo;
}