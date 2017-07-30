function Sll(){
  this.head = null;
  this._length = 0;
}
function Node(value){
  this.val = value;
  this.next = null;
}
Sll.prototype.add = function(value) {
    var node = new Node(value),
        currentNode = this.head;
        if (!currentNode) {
       this.head = node;
       this._length++;

       return node;
   }
}
console.log(Sll);


sll.prototype.add = function(value){
  var mynode = new Node(value);
  if(!this.head){
    this.head = mynode
  }else{
    var curr = this.head
    while(curr.next){
      curr = curr.next
    }
    curr.next = myNode
  }

}
]
