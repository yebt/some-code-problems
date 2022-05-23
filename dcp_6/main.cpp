#include <iostream>
#include <stdint.h>

using namespace std;

// XOR LIST
class XORLinkList {
public:
    int value;
    int length=0;
    XORLinkList* headP = nullptr;
    XORLinkList* linkP;

    XORLinkList(int newV){
        this->value = newV;
        this->linkP = pxor(this->headP, nullptr);
        this->headP = this;
        this->length=1;
    }

    /**
    * This function add a new calue to the list
    */
    void add(int value){
        XORLinkList* newNode = new XORLinkList(value);
        newNode->linkP = pxor(this->headP,nullptr);
        this->headP->linkP = pxor(newNode, pxor(this->headP->linkP,nullptr));
        this->headP = newNode;
        this->length +=1;
    }


    /**
    * get the value of an index
    */
    XORLinkList* get (int indx){
        if (indx < 0){
            return nullptr;
        }
        // vars to operate an travel
        XORLinkList* current = this->headP;
        XORLinkList* prev = nullptr;
        XORLinkList* next;

        int counter = 0;
        while( this->length - counter -1 > indx && current != nullptr){
            next = pxor(prev, current->linkP);
            prev = current;
            current = next;
            counter++;
        }

        return current;
    }

    /** 
    * Traverse by list
    */
    void Traverse(){
        XORLinkList* curr = this->headP; // se arume que estamos parados en la cabecera
        XORLinkList* prev = nullptr; // el anterior a la cabecera siempre será null
        XORLinkList* next; // el siguinete no lo conocemos

        while (curr != nullptr) {
            std::cout << curr->value << " <->=> ";
            next = pxor(prev, curr->linkP);
            // change  references
            prev = curr;
            curr = next;
        }
        std::cout <<  "nullptr" << std::endl;
    }

    /**
    * Operate tho pointers with xop preration
    */
    static XORLinkList* pxor(XORLinkList* x, XORLinkList* y){
        return (XORLinkList*)((uintptr_t)(x) ^ (uintptr_t)(y) );
    }

};


int main(int argc, char *argv[])
{

    XORLinkList* xl = new XORLinkList(23);
    xl->add(3);
    xl->add(1);
    xl->add(43);
    std::cout << "XL:" << std::endl;
    xl->Traverse();
    std::cout << "Xl[2] : " << xl->get(2)->value << std::endl; 
    std::cout << "Xl[0] : " << xl->get(0)->value << std::endl; 
    return 0;
}
