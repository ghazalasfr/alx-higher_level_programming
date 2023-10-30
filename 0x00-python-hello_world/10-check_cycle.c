#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - Checks if a singly linked list has a cycle in it
  * @list: The singly linked list to check
  *
  * Return: 1 if it has a cycle, 0 if not
  */
int check_cycle(listint_t *list) {
        listint_t *list1 = list, *list2 = list;

        while (list2 && list2->next) {
                list1 = list1->next;
                list2 = list2->next->next;

                if (list1 == list2)
                    return 1;
        }

        return 0;
}
