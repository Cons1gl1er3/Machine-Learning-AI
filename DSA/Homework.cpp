#include<bits/stdc++.h>
using namespace std;

#define SIZE 10000

typedef struct Node{
    int value;
    Node* next = NULL;
}Node;

int loga(long long n){
    int res = 0;
    while (n>1){
        n/=10;
        res++;
    }
    return res;
}

int find_(unordered_map<int, Node*> hashmap, int key, int val){
    if (hashmap.find(key) == hashmap.end()){
        return 0;
    }
    else {
        Node* p = hashmap[key];
        while (p!=NULL){
            if (p->value == val) {
                return 1;
            }
            p = p->next;
        }
        return 0;
    }
}

int insert(unordered_map<int, Node*> hashmap, int key, int val){
    if (find_(hashmap, key, val)) return 0;
    else{
        Node* p = new Node;
        p->value = val;
        hashmap[key] = p;
        return 1;
    }
}

int main(){
    unordered_map<int, Node*> hashmap;
    long long n;
    string s;
    while (1){
        cin >> s;
        if (s == "*") break;
        n = stoll(s);
        int key = (int)n%SIZE;
        Node* p = new Node;
        p->value = loga(n);
        if (hashmap.find(key) == hashmap.end()){
            hashmap[key] = p;
        }
        else{
            Node* cur = hashmap[key];
            while (cur->next!=NULL) cur = cur->next;
            cur->next = p;
        }
    }

    while (1){
        cin >> s;
        long long n;
        int key = (int)n%SIZE;
        int val = loga(n);
        if (s=="***") break;
        else if (s=="find"){
            cout << find_(hashmap, key, val) << endl;
        }
        else if (s=="insert"){
            cout << insert(hashmap, key, val) << endl;
        }
    }
}
