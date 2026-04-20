#!/usr/bin/env python3
import sys
from collections import deque

def main():
    print("Hi Jaanu, just want to say I love you", end=" ")

    for i in range(1, sys.maxsize):
        if i == sys.maxsize - 1:  # Just to avoid actually running forever 😅
            print(f"{i} much :) <3")
            break

    # Dictionary/HashMap of all your amazing qualities
    jaanu_ratings = {
        "looks": "10",
        "personality": "10",
        "smile": "10",
        "work_ethic": "10",
        "skin": "10",
        "culture": "10",
        "fashion": "10",
        "her_person": "me"
    }

    print("\nHere's my official rating system for you:")
    for quality, rating in jaanu_ratings.items():
        if quality == "her_person":
            print(f"{quality}: {rating} ❤️")
        else:
            print(f"{quality}: {rating}/10 ⭐")

    # Stack of places we've been together
    places_weve_fucked = []  # Using list as stack
    places_weve_fucked.append("LA")      # push
    places_weve_fucked.append("Hawaii")  # push
    places_weve_fucked.append("Vancouver")  # push

    print(f"\nOur travel stack (LIFO) - places we've made memories:")
    temp_stack = places_weve_fucked.copy()
    while temp_stack:
        place = temp_stack.pop()  # pop from stack
        print(f"  📍 {place}")

    # Queue of places we plan to make love
    places_we_plan_to_make_love = deque()  # Using deque as queue
    romantic_destinations = ["London", "Paris", "Mykonos", "Milos",
                           "Chicago", "Vegas", "NYC", "Bali", "Japan"]

    for destination in romantic_destinations:
        places_we_plan_to_make_love.append(destination)  # enqueue

    print(f"\nOur romance queue (FIFO) - places we're gonna make love 😏:")
    temp_queue = places_we_plan_to_make_love.copy()
    while temp_queue:
        place = temp_queue.popleft()  # dequeue from front
        print(f"  🌹 {place}")

    # Sweet ending message
    print("\nI did this all during this interview because I was bored as fuck but ILY meri Nameerah 💖")
    print("\nP.S. - Hope you appreciate my use of data structures to express my love 🤓❤️")

if __name__ == "__main__":
    main()
