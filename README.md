# Gilded-Rose-Refactoring-Kata

## Overview
The Guilded Rose challenge is a coding exercise that involves updating the quality of items in a shop based on specific rules. This repository contains a straightforward solution that effectively addresses the problem without unnecessary complexity.

## Solution Approach

In this implementation, I focused on simplicity and clarity. The goal was to create a solution that is easy to understand and maintain, demonstrating that not every problem requires an over-engineered approach.
Key Features of the Solution

    Quality Constraints and Handling Edge Cases: The constrain_quality method ensures that the quality of items remains within the valid range of 0 to 50. This prevents any invalid quality values from affecting the overall logic and reducing redundancy.
    
    Item Update Logic: The update_quality method iterates through the list of items and applies the appropriate quality adjustments based on the item type and its sell_in value. The use of a # match statement (Python 3.10+) allows for clear and concise handling of different item types.

## Conclusion
This solution demonstrates that a clear and simple approach can effectively solve the problem at hand. By focusing on the essential requirements and avoiding unnecessary complexity, we can create maintainable and understandable code.

Feel free to explore the code and adapt it for your own needs!
