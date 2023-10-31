#include "lists.h"
#include <stdlib.h>

/**
  * insert_node - Inserts a number into a sorted singly linked list
  * @head: The head of the sorted singly linked list
  * @number: The number to be inserted in the singly linked list
  *
  * Return: The singly linked list with the new number added
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *temp = NULL;

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!current || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (*head);
	}

	while (current->next && current->next->n < number)
		current = current->next;

	temp = current->next;
	current->next = new_node;
	new_node->next = temp;

	return (*head);
}
