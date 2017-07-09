# uv-poll
It's like UV_POLL_T but javascript

This is ripped from [node serialport](https://github.com/EmergingTechnologyAdvisors/node-serialport) internals. It's an event emitter wrapper for [libuv's UV_POLL_T struct](http://docs.libuv.org/en/v1.x/poll.html).

The underlying event stream is continuous so instead of emitting all of them we ask for the next one. This can be done two ways.

- `poll.once(event, callback)` this automatically calls `poll()` for the correct event
- `poll.poll(eventInt)` asks `uv_poll_start` to poll for these additional events

```js
const fd = fs.openSync('file')
const poll = new Poller(fd)
poll.once('readable', () => console.log(`fd ${fd} is now readable`))
poll.once('writable', () => console.log(`fd ${fd} is now writable`))
poll.once('disconnect', () => console.log(`fd ${fd} is now disconnect`)) // means not readable or writable
```

This is tested pretty heavily in serialport. Happy to land any any improvements, tests, or fixes.
