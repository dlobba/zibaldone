/*
	Thanks to: http://arnold.uthar.net/index.php?n=Work.TemplatesC
*/
#include <stdlib.h>
#include <stdio.h>

#define DEFINE_QUEUE(type) struct Node {type value;};

DEFINE_QUEUE(int)

/*
	This way we can declare a Node whose value can be anything
	(with some modification...)
	
	But we cannot declare more than one QUEUE. Why?
	
	Whene we call DEFINE_QUEUE(int) the preprocessore
	change that call with struct Node {type value};
	if we call DEFINE_QUEUE(char) later, it does the same thing
	but now there are two structs called Node with differenct value types.
*/

int
main(int argc, char** argv) {

	struct Node n = { .value = 3 };

	printf("%d", n.value);
	
	// needed just for non terminal execution (so just for windows/VS)
	getchar();

	return 0;
}