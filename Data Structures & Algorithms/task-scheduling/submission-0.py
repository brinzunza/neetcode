class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        
        pqueue = [-count for count in count.values()]
        heapq.heapify(pqueue)

        total_time = 0
        cooldown_queue = deque()

        while pqueue or cooldown_queue:
            total_time += 1

            if pqueue:
                remaining_count = heapq.heappop(pqueue)
                remaining_count += 1

                if remaining_count != 0:
                    next_available_time = total_time + n
                    cooldown_queue.append([remaining_count, next_available_time])
            
            if cooldown_queue and cooldown_queue[0][1] == total_time:
                ready_task_count = cooldown_queue.popleft()[0]
                heapq.heappush(pqueue, ready_task_count)

        return total_time