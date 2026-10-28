import heapq


def connect_cables(lengths):
    """Повертає мінімальні витрати та порядок з'єднань."""
    heap = list(lengths)
    heapq.heapify(heap)

    total_cost = 0
    connections = []

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        combined = first + second
        total_cost += combined
        connections.append((first, second, combined))

        heapq.heappush(heap, combined)

    return total_cost, connections


# Приклад використання
lengths = [4, 3, 2, 6]
total_cost, connections = connect_cables(lengths)

for first, second, combined in connections:
    print(f"{first} + {second} = {combined}")

print(f"Мінімальні загальні витрати: {total_cost}")