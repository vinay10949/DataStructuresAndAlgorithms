package main

import "fmt"

type maxHeap struct {
	arr []int
}

func newMaxHeap(arr []int) *maxHeap {
	maxHeap := &maxHeap{
		arr: arr,
	}
	return maxHeap
}

func (m *maxHeap) leftchildIndex(index int) int {
	return 2*index + 1
}

func (m *maxHeap) rightchildIndex(index int) int {
	return 2*index + 2
}

func (m *maxHeap) swap(first, second int) {
	temp := m.arr[first]
	m.arr[first] = m.arr[second]
	m.arr[second] = temp
}

func (m *maxHeap) leaf(index int, size int) bool {
	if index >= (size/2) && index <= size {
		return true
	}
	return false
}

func (m *maxHeap) downHeapify(current int, size int) {
	if m.leaf(current, size) {
		return
	}
	smallest := current
	leftChildIndex := m.leftchildIndex(current)
	rightRightIndex := m.rightchildIndex(current)
	if leftChildIndex < size && m.arr[leftChildIndex] < m.arr[smallest] {
		smallest = leftChildIndex
	}
	if rightRightIndex < size && m.arr[rightRightIndex] < m.arr[smallest] {
		smallest = rightRightIndex
	}
	if smallest != current {
		m.swap(current, smallest)
		m.downHeapify(smallest, size)
	}
	return
}

func (m *maxHeap) buildMaxHeap(size int) {
	for index := ((size / 2) - 1); index >= 0; index-- {
		m.downHeapify(index, size)
	}
}

func (m *maxHeap) sort(size int) {
	m.buildMaxHeap(size)
	for i := size - 1; i > 0; i-- {
		// Move current root to end
		m.swap(0, i)
		m.downHeapify(0, i)
	}
}

func (m *maxHeap) print() {
	for _, val := range m.arr {
		fmt.Println(val)
	}
}

func main() {
	inputArray := []int{6, 5, 3, 7, 2, 8, -1}
	maxHeap := newMaxHeap(inputArray)
	maxHeap.sort(len(inputArray))
	maxHeap.print()

}