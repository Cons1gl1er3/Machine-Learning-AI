#include<iostream>
using namespace std;

#define MAX 10

typedef struct Queue{
    int items[MAX];
    int front = -1, rear = -1;
}qu;

bool isEmpty(qu* q){
    return q->front == -1;
}

bool isFull(qu* q){
    return (q->rear == MAX - 1);
}

void enqueue(qu* q, int newItem){
    if (isFull(q)){
        printf("Full queue!\n");
        return;
    }
    if (q->front == -1) q->front = 0;
    q->rear++;
    q->items[q->rear] = newItem;
}

void dequeue(qu* q){
    if(isEmpty(q)){
        printf("Empty queue!\n");
        return;
    }
    q->front++;
    if (q->front>q->rear){
        q->front = -1;
        q->rear = -1;
    }
}

void printQueue(qu* q){
    if (isEmpty(q)){
        printf("Empty queue!\n");
        return;
    }
    for (int i=q->front; i<=q->rear; i++){
        printf("%d ", q->items[i]);
    }
    printf("\n");
}

int main(){
    qu* q = new qu;
    enqueue(q, 1);
    enqueue(q, 2);
    printQueue(q);
    dequeue(q);
    printQueue(q);
}
