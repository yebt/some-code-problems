#include <iostream>
#include <stdint.h>

using namespace std;

// XOR LIST
class XORLinkList {
public:
    int value;
    XORLinkList* headP;
    XORLinkList* linkP;

    XORLinkList(int newV){
        this->value = newV;
        this->headP = this;
    }

    void add(int value){
        XORLinkList* newNode = new XORLinkList(value);
        // padre xor siguiente
        newNode->linkP= pxor(this->headP, nullptr);
        this->headP->linkP = pxor(newNode, pxor(this->headP, nullptr));
        // como soy el padre no tengo padre, pero si siguiente
        this->headP = newNode;
    }

    XORLinkList* get (int indx){
        // vars to operate an travel
        XORLinkList* current = this->headP;
        XORLinkList* prev = nullptr;
        XORLinkList* next;

        while(indx > 0 && current != nullptr){
            next = pxor(prev, current->linkP);
            prev = current;
            current = next;
            indx --;
        }

        return current;
    }

private:
    XORLinkList* pxor(XORLinkList* x, XORLinkList* y){
        return (XORLinkList*)((uintptr_t)(x) ^ (uintptr_t)(x) );
    }
};


int main(int argc, char *argv[])
{

    XORLinkList* xl = new XORLinkList(23);
    xl->add(3);
    xl->add(1);
    xl->add(43);
    std::cout << xl->get(1)->value << std::endl; 
    return 0;
}
