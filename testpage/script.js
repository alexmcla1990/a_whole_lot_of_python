const draggables = document.querySelectorAll(".draggable");
const containers = document.querySelectorAll(".container");

draggables.forEach((draggable) => {
  draggable.addEventListener("dragstart", () => {
    draggable.classList.add("dragging");
    console.log("drag start");
  });
  draggable.addEventListener("dragend", () => {
    draggable.classList.remove("dragging");
  });
});

containers.forEach((container) => {
  container.addEventListener("dragover", (e) => {
    e.preventDefault();
    const afterElement = getDragAfterElement(container, e.clientY);
    const draggable = document.querySelector(".dragging");
    if (afterElement == null) {
      container.appendChild(draggable);
    } else {
      container.insertBefore(draggable, afterElement);
    }
  });
});

function getDragAfterElement(container, y) {
  const draggableElements = [
    ...container.querySelectorAll(".draggable:not(.dragging)"),
  ];
  return draggableElements.reduce(
    (closest, child) => {
      const box = child.getBoundingClientRect();
      const offset = y - box.top - box.height / 2;
      console.log(offset);
      if (offset < 0 && offset > closest.offset) {
        return { offset: offset, element: child };
      } else {
        return closest;
      }
    },
    { offset: Number.NEGATIVE_INFINITY }
  ).element;
}

/*Touch screen drag and drop notes 
touchstart, touchend, touchmove, touchcancel
document.querySelector('p').addEventListener('touchstart', f);
function f(ev){
    console.log(ev.touches, ev.type)
}
-------------------------------------
/*This code is not doing anything yet. Trying to get items to become draggable on mobile device */
/*select the thing
window.onload = function() {
var draggableitem = document.getElementById('box');
/*add your listene
draggableitem.addEventListener('touchmove', function(ev){
 /*find the location
    var touchLocation = ev.targetTouches[0];
/*give element new coordinates
    draggableitem.style.left = touchLocation.pageX = 'px';
    draggalbeitem.style.top = touchLocation.pageY = 'px';
})
}
/*
creating a finite space for draggable item 
draggableitem.addEventListener('touchend', function(ev){
var x = parseInt(draggableitem.style.left);
var y = parseInt(draggableitem.style.top);
if ( x < number || x > number){
    draggableitem.style.left = 'px';
    draggableitem.style.top = 'px';
}
})
/*const select_items = document.querySelectorAll('.selection');
const container = document.querySelectorAll('.container')
let draggedItem = null;
for (let i = 0; i < select_items.length; i++) {
    const item = select_items[i];
    
    item.addEventListener('dragstart', function () {
        draggedItem = this;
        setTimeout(function(){
                this.style.display = 'none';
        }, 0);
        console.log('dragstart', e);
    });
    item.addEventListener('dragend', function(){
        console.log('dragend');
        setTimeout(function (){
            draggedItem.style.display = 'block';
            draggedItem = null;
        }, 0);
    });
    for (let j = 0; j < columns.length; j ++) {
        const columns = columns[i];
        container.addEventListener('dragover', function(e){
            e.preventdefault();
        });
        container.addEventListener('dragenter', function(e){
            e.preventdefault();
        });
        container.addEventListener('drop', function(e) {
            this.append(draggedItem);
        });
    }
}
*/

/*$(function () {
    $(window).on('scroll', function () {
        if ( $(window).scrollTop() > 10 ) {
            $('.navbar').addClass('active');
        } else {
            $('.navbar').removeClass('active');
        }
    });
});
const myHeading = document.getElementById('myHeading');
myHeading.addEventListener('click', () => {
             myHeading.style.color = 'red';              
                           });
                           /*
<button id="myButton">Make heading red</button>
<input type="text" id="myTextInput">
*/
/*
const myButton = document.getElementsById('myButton');
}
myButton.addEventListener('click', () => {
             myHeading.style.color = myTextInput.value;              
                           });
            
                           var button = document.getElementById('sayPhrase');
                           var input = document.getElementById('phraseText');
                           
                           const myList = document.getElementsByTagName('li');
for (let i = 0; i < myLife.length; i += 1) {
    myList[i].style.color = 'purple';
    const errorNotPurple = document.getElementsByClassName('error-not-purple');
    for (let i = 0; i < errorNotPurple.length; i += 1){
        errorNotPurple[i].style.color = 'red';
    }
    document.querySelectorAll('li')
    document.querySelector('')
    */

// function to enable/disable DnD Source
//function dndSource(params: DndSourceCallbackParams) => boolean;
/*
// interface for params
interface DndSourceCallbackParams {
    node: RowNode;
    data: any;
    column: Column;
    colDef: ColDef;
    context: any;
    api: GridApi;
    columnApi: ColumnApi;*/
