
const Heap = require("collections/heap")


const comparator = function(a, b) { return b.priority - a.priority }
const taskQueue = new Heap(null, null, comparator)


taskQueue.push({'priority':7, 'letter':'g'})
taskQueue.push({'priority':1, 'letter':'a'})
taskQueue.push({'priority':4, 'letter':'d'})
taskQueue.push({'priority':5, 'letter':'e'})
taskQueue.push({'priority':3, 'letter':'c'})
taskQueue.push({'priority':6, 'letter':'f'})
taskQueue.push({'priority':2, 'letter':'b'})



while(taskQueue.length > 0) {
	const task = taskQueue.pop()
	console.log(task.letter)
}