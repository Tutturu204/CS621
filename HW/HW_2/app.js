
var organizedByTag = function(toDoObjects) {
    var tags = [];
    
    toDoObjects.forEach(function (toDo) {
    
        toDo.tags.forEach(function (tag) {
            
            
            if (tags.indexOf(tag) === -1) {
                tags.push(tag);
            }
        });
    });
    console.log(tags);

    var tagObjects = tags.map(function (tag) {
       
        var toDosWithTag = [];
        toDoObjects.forEach(function (toDo) {
            
            if (toDo.tags.indexOf(tag) !== -1) {
                toDosWithTag.push(toDo.description);
            }
        });
       
        return { "name": tag, "toDos": toDosWithTag };
    });
    return tagObjects;
    
};

var main = function (toDoObjects) {
    "use strict";


    var toDos = toDoObjects.map(function (toDo) {
        // we'll just return the description
        // of this toDoObject
        return toDo.description;
        });

    var makeTabActive = function (tabNumber) {
        
        var tabSelector = ".tabs a:nth-child(" + tabNumber + ") span";
        var $content;
        var $input, $button;
        var i;

        $(".tabs span").removeClass("active");
        $(tabSelector).addClass("active");
        $("main .content").empty();
        
        if ($(tabSelector).parent().is(":nth-child(1)")) {
            $content = $("<ul>");
            for (i = toDos.length-1; i >= 0; i--) {
                $content.append($("<li>").text(toDos[i]));
            }
            $("main .content").append($content);
        }
        else if ($(tabSelector).parent().is(":nth-child(2)")) {
            
            $content = $("<ul>");
            
            toDos.forEach(function (todo) {
                $content.append($("<li>").text(todo));
            });
            $("main .content").append($content);
            
            
        }

        else if ($(tabSelector).parent().is(":nth-child(3)")) {
            console.log("the tags tab was clicked!");
            //list of objects
            var organizeByTag = organizedByTag(toDoObjects);
              
           organizeByTag.forEach(function (tag) {
                var $tagName = $("<h3>").text(tag.name);
                $content = $("<ul>");
            
                  
                tag.toDos.forEach(function (description) {
                    var $li = $("<li>").text(description);
                    $content.append($li);
                });
                
                $("main .content").append($tagName);
                $("main .content").append($content);
            });
            
            console.log("the tags tab was clicked!");
        }

        else if ($(tabSelector).parent().is(":nth-child(4)")) {
            var $input = $("<input>").addClass("description"),
            $inputLabel = $("<p>").text("Description: "),
            $tagInput = $("<input>").addClass("tags"),
            $tagLabel = $("<p>").text("Tags: "),
            $button = $("<button>").text("+");

            $button.on("click", function () {
                var description = $input.val(),
                tags = $tagInput.val().split(",");
                newToDo = {"description" : description, "tags" : tags }
                //toDoObjects.push({"description":description, "tags":tags});

                $.post("todos", newToDo, function (response) {
                    // this callback is called with the server responds
                    console.log("We posted and the server responded!");
                    console.log(response);
                    toDoObjects.push(newToDo);
                   

                    toDos = toDoObjects.map(function (toDo) {
                        return toDo.description;
                    });
                    $input.val("");
                    $tagInput.val("");
                });

            });

            $content = $("<div>").append($inputLabel).append($input).append($tagLabel).append($tagInput).append($button);
            $("main .content").append($content);
            
        };
    };

    $(".tabs a:nth-child(1)").on("click", function () {
        makeTabActive(1);
        return false;
    });
    
    $(".tabs a:nth-child(2)").on("click", function () {
        makeTabActive(2);
        return false;
    });
    
    $(".tabs a:nth-child(3)").on("click", function () {
        makeTabActive(3);
        return false;
    });

    $(".tabs a:nth-child(4)").on("click", function () {
        makeTabActive(4);
        return false;
    });


};


$(document).ready(function () {
    $.getJSON("products.json", function (toDoObjects){
        main(toDoObjects);
    });
});

