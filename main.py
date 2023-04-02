from collections import namedtuple

# Define a named tuple to represent a job assigned to a worker
AssignedJob = namedtuple('AssignedJob', ['worker', 'started_at'])

# Define a class to represent a job queue
class JobQueue:
    def __init__(self, n_workers, jobs):
        self.n = n_workers
        self.jobs = jobs
        self.finish_time = [] # A list to store the finish time of each worker
        self.assigned_jobs = [] # A list to store the assigned jobs
        for i in range(self.n):
            self.finish_time.append([i, 0]) # Initialize the finish time of each worker to 0

    # A helper function to sift down an element in the heap
    def SiftDown(self, i):
        min_index = i
        left = 2 * i + 1 # The index of the left child
        right = 2 * i + 2 # The index of the right child
        if left < self.n:
            # If the finish time of the left child is smaller than the current element's finish time
            if self.finish_time[min_index][1] > self.finish_time[left][1]:
                min_index = left
            # If the finish time of the left child is the same as the current element's finish time
            elif self.finish_time[min_index][1] == self.finish_time[left][1]:
                # If the index of the left child is smaller than the current element's index
                if self.finish_time[min_index][0] > self.finish_time[left][0]:
                    min_index = left
        if right < self.n:
            # If the finish time of the right child is smaller than the current element's finish time
            if self.finish_time[min_index][1] > self.finish_time[right][1]:
                min_index = right
            # If the finish time of the right child is the same as the current element's finish time
            elif self.finish_time[min_index][1] == self.finish_time[right][1]:
                # If the index of the right child is smaller than the current element's index
                if self.finish_time[min_index][0] > self.finish_time[right][0]:
                    min_index = right
        if min_index != i:
            # Swap the current element with the minimum child element
            self.finish_time[i], self.finish_time[min_index] = self.finish_time[min_index], self.finish_time[i]
            # Recursively sift down the element
            self.SiftDown(min_index)

    # A function to assign the next job to the worker who finishes earliest
    def NextWorker(self, job):
        root = self.finish_time[0] # Get the root of the heap, which has the smallest finish time
        next_worker = root[0] # Get the index of the worker with the smallest finish time
        started_at = root[1] # Get the finish time of the worker with the smallest finish time
        self.assigned_jobs.append(AssignedJob(next_worker,started_at)) # Add the assigned job to the list of assigned jobs
        self.finish_time[0][1] += job # Update the finish time of the worker who finished earliest
        self.SiftDown(0) # Sift down the root element to maintain the heap property

# The main function that takes input, creates a JobQueue instance, assigns jobs to workers, and prints the assigned jobs
def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    
    job_queue = JobQueue(n_workers, jobs)
    for job in jobs:
        job_queue.NextWorker(job)
    assigned_jobs = job_queue.assigned_jobs

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
