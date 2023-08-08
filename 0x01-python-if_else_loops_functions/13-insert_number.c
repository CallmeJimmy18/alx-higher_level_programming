#include "lists.h"
/**
 * insert_node - this inserts a new node
 * @head: this is the head pointer
 * @number: this is the number we want to insert
 * Return: address of node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = head;
	listint_t *ptr2 = malloc(sizeof(listint_t));
	ptr2->n = number;
	ptr2->next = NULL;

	while (ptr->n < number)
	{
		ptr = ptr->next;
		pos++;
	}
	ptr2->next = ptr->next;
	ptr->next = ptr2;
}

