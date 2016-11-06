/*
Thanks to: http://arnold.uthar.net/index.php?n=Work.TemplatesC
*/
#include <stdlib.h>
#include <stdio.h>

/*
Use preprocessor concatenation '##' to change at runtime the
string associated at the Node struct.

This way we can make Node of different types.
*/
#define DEFINE_NODE(type) struct Node_##type {type value;};

DEFINE_NODE(int)
DEFINE_NODE(char)

int
main(int argc, char** argv) {

	struct Node_int n = { .value = 3 };
	struct Node_char c = { .value = 'a' };

	printf("%d\n", n.value);
	printf("%c\n", c.value);

	// needed just for non terminal execution (so just for windows/VS)
	getchar();

	return 0;
}