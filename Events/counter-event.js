const EventEmitter = require('node:events');

class Counter extends EventEmitter {
    count = 0

    increment(){
        this.count++;
    }

    decrement(){
        this.count--;
    }

    print(){
        console.log(`Count: ${this.count}`)
    }
}

const count = new Counter()

count.on("increment", function(){
    this.increment()
})

count.on("decrement", function(){
    this.decrement()
})


count.emit("increment")
count.emit("increment")
count.print() // prints 2
count.emit("decrement")
count.print() // prints 1
