#include "lists.h"

/**
 *insert_node - insert a node at a sorted linked list
 *@head: head of linked list
 *@number: the number to be inserted
 *
 *Return: adress of the new node on success, NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		new->n = number;
		*head = new;
		return (new);
	}
	current = *head;
	while (current->next != NULL)
	{
		if (current->next->n >= number)
		{
			new->next = current->next;
			current->next = new;
			new->n = number;
			return (new);
		}
		current = current->next;
	}
	new = add_nodeint_end(head, number);
	return (new);
}
