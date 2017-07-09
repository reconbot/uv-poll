const assert = require('assert')
const Poller = require('../')
const PollerBinding = require('bindings')('poller.node').Poller;

describe('Poller Bindings', () => {
  it('constructs', () => {
    assert(new PollerBinding(1, () => {}))
  })
})

describe('Poller', () => {
  it('constructs', () => {
    assert(new Poller(1))
  })
})
