#include "lists.h"

/**
 * insert_node - is a function that inserting a number in linked list
 * @head: is the head of linked list
 * @number: id the number to be inserted
 * Return: NULL If Fails Or Pointer If Success
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *nw;

	nw = malloc(sizeof(listint_t));
	if (nw == NULL)
		return (NULL);
	nw->n = number;

	if (node == NULL || node->n >= number)
	{
		nw->next = node;
		*head = nw;
		return (nw);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;

	nw->next = node->next;
	node->next = nw;
	return (nw);
}
