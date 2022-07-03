var express = require("express"),
    http = require("http"),
    app = express(),
    toDos = {
    // set up todo list here by copying
    // the content from todos.OLD.json
    };
app.use(express.static(__dirname));
app.use(express.urlencoded({extended:false}));
http.createServer(app).listen(3000);
/*
app.get("products.json", function (req, res) {
    res.json(toDos);
});
*/
app.post("/todos", function (req, res) {
    var newToDo = req.body;
    console.log(newToDo);
    toDos.push(newToDo);
    // send back a simple object
    res.json({"message":"You posted to the server!"});
    });