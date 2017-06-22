def batch_iter(my_iter, num_per_batch=20, limit=None):
    from itertools import islice
    start_index =0
    while start_index<limit:
        try:
            yield [row for row in islice(my_iter,num_per_batch)]
            start_index += num_per_batch
        except StopIteration as e:
            return []
