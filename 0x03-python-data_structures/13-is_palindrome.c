#include "lists.h"
#include <stdio.h>

void reverse_list(listint_t **head);
int compare_lists(listint_t *list1, listint_t *list2);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev_slow, *mid, *second_half;
    int palindrome = 1;

    slow = *head;
    fast = *head;
    prev_slow = NULL;

    // Find the middle of the linked list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        // Save the previous of the slow pointer
        prev_slow = slow;

        slow = slow->next;
    }

    // If the list has odd number of elements, ignore the middle element
    mid = slow;
    if (fast != NULL)
    {
        slow = slow->next;
    }

    // Reverse the second half of the linked list
    reverse_list(&second_half);

    // Compare the first and second halves of the linked list
    palindrome = compare_lists(*head, second_half);

    // Restore the reversed second half back to its original state
    reverse_list(&second_half);

    // If the list had an odd number of elements, reconnect the middle element
    if (mid != NULL)
    {
        prev_slow->next = mid;
        mid->next = second_half;
    }
    else
    {
        prev_slow->next = second_half;
    }

    return palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
    listint_t *prev, *current, *next;

    prev = NULL;
    current = *head;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @list1: first linked list
 * @list2: second linked list
 * Return: 1 if the lists are identical, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
        {
            return 0; // Not a palindrome
        }

        list1 = list1->next;
        list2 = list2->next;
    }

    // If both lists are empty or reached the end, they are identical
    return (list1 == NULL && list2 == NULL);
}

