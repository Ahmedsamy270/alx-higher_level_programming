#include "lists.h"

/**
 * check_cycle - is a function that checks for the loop in linked list
 * @list: is the head of the linked list
 * Return: 0 If Not Cycled Or 1 If True
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
	{
		return (0);
	}
	slow = list;
	fast = list->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
