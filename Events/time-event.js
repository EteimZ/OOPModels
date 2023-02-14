const EventEmitter = require('node:events');

class Timer extends EventEmitter {

    constructor(){
        super();
        this.intervalId = null;
    }

    start(){
        // bind currentTime method to the class instance
        this.intervalId = setInterval(this.currentTime.bind(this), 1000);
    }

    stop(){
        clearInterval(this.intervalId);
    }

    currentTime() {
        const currentTime = new Date();
        const hours = currentTime.getHours();
        const minutes = currentTime.getMinutes();
        const seconds = currentTime.getSeconds();

        const result = `The time is: ${hours}:${minutes}:${seconds}`
        this.emit("current_time", result);
    }
}

const timer = new Timer();

timer.on("current_time", function(time) {
    console.log(time);
});

timer.start();

// Stop the timer after 10 seconds
setTimeout(function() {
    timer.stop();
}, 10000);
