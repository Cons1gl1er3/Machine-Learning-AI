#include<iostream>
using namespace std;

typedef struct Node{
    int value;
    Node* left = NULL;
    Node* right = NULL;
}Node;

string check_type_tree(Node* root){
    if (is_full_binary_tree(root)) return "Full Binary Tree";
    if (is_perfect_binary_tree(root)) return "Perfect Binary Tree";
    // Complete tree
    // Balance tree
}

bool is_full_binary_tree(Node* root){
    // Check for emptiness first
    if (root == NULL) return true;
    if (root->left == NULL && root->right == NULL) return true;
    if (root->left != NULL && root->right != NULL) return (is_full_binary_tree(root->left) && is_full_binary_tree(root->right));
    return false;
}

// Check if perfect binary tree
int depth(Node *node) {
  int d = 0;
  while (node != NULL) {
    d++;
    node = node->left;
  }
  return d;
}

bool isPerfectR(struct Node *root, int d, int level = 0) {
  if (root == NULL)
    return true;

  if (root->left == NULL && root->right == NULL)
    return (d == level + 1);

  if (root->left == NULL || root->right == NULL)
    return false;

  return isPerfectR(root->left, d, level + 1) &&
       isPerfectR(root->right, d, level + 1);
}

bool is_perfect_binary_tree(Node *root) {
  int d = depth(root);
  return isPerfectR(root, d);
}

int main(){
    return 1;
}