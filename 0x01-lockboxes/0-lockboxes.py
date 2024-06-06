#!/usr/bin/python3
'''ockboxes.
'''

def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys.
    '''
    total_boxes = len(boxes)
    opened_boxes = set([0])
    keys_to_check = set(boxes[0])

    while keys_to_check:
        current_key = keys_to_check.pop()
        if current_key < 0 or current_key >= total_boxes:
            continue
        if current_key not in opened_boxes:
            keys_to_check.update(boxes[current_key])
            opened_boxes.add(current_key)

    return len(opened_boxes) == total_boxes

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
