#include<bits/stdc++.h>
using namespace std;

#define MAX 10

typedef struct stack{
    int items[MAX];
    int top;
}st;

void createEmptyStack(st* s){
    s->top = -1;
}

bool isEmpty(st* s){
    return s->top == -1;
}

bool isFull(st* s){
    return s->top == MAX - 1;
}

void push(st* s, int newItem){
    if (isFull(s)) return;
    s->top++;
    s->items[s->top] = newItem;
}

void pop(st* s){
    if (isEmpty(s)) return;
    s->top--; 
}

void printStack(st* s){
    if (isEmpty(s)) printf("Empty stack\n");
    while (s->top>-1){
        printf("%d ",s->items[s->top]);
        s->top--;
    }
}

int main(){
    st* s = new st;
    createEmptyStack(s);
    push(s, 1);
    push(s, 2);
    printStack(s);
}
