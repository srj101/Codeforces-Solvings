#include<stdio.h> 
#include<stdlib.h>
struct newNode
{
  int data;
  struct newNode *next;
};
struct newNode *head;
struct newNode *cur;

void insert(int value)
{
   struct newNode *node;
   node = (struct newNode*) malloc(sizeof(struct newNode));
   node->data = value;
   node->next = NULL;
   if(head == NULL)
  head = node, cur=head;
  
   else
   {
      struct newNode *temp = cur;
      while(temp->next != NULL)
        temp = temp->next;
         temp->next = node;
   }

}
void insertBetween(int value, int loc1, int loc2)
{
   struct newNode *node;
   node = (struct newNode*)malloc(sizeof(struct newNode));
   node->data = value;
   if(head == NULL)
   {
      node->next = NULL;
      head = node;
   }
   else
   {
      struct newNode *temp = head;
      while(temp->data != loc1 && temp->data != loc2)
    temp = temp->next;
        node->next = temp->next;
      temp->next = node;
   }

}
int check()
{
  struct newNode *p;
  p = cur;
  while(p != NULL)
  {
    if(p->data==117)
    return 1;
      p = p->next;
  }
  return 0;
}

void display()
{
  struct newNode *p;
  p = cur;
  while(p != NULL)
  {
    printf("%d ", p->data);
      p = p->next;
  }
}


int main()
{
  insert(10);
  insert(9);
  insert(5);
  insert(3);
  printf("Before The Inserting: ");
  display();
  
  insertBetween(117,5,3);
  printf("\nAfter The Inserting: ");
  display();
  
  if(check())
  {
    printf("\nFound!!");
  }
  else
  {
    printf("\nNOT Found.");
  }
}