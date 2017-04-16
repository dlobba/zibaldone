#define GLEW_STATIC
#include <GL\glew.h>
#include <GLFW\glfw3.h>

#include <stdio.h>

const GLchar* shaderSource =
    //"#version 330 core"
    "layout (location = 0) in vec3 position;"
    "void main ()"
    "{"
        "gl_Position = vec4 (position.x, position.y, position.z, 1.0);"
    "}";

const GLchar* fragmentSource =
    //"#version 330 core"
    "out vec4 color;"
    "void main ()"
    "{"
        "color = vec4 (1.0f, 0.5f, 0.2f, 1.0f);"
    "}";


int main () {
	glfwInit ();
	glfwWindowHint (GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint (GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint (GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
	glfwWindowHint (GLFW_RESIZABLE, GL_FALSE);

	GLFWwindow* window = glfwCreateWindow (800, 600, "Opengl test", NULL, NULL);
	if (window == NULL) {
		printf ("Failed to create GLFW window.\n");
        glfwTerminate ();
        return -1;
	}

    glfwMakeContextCurrent (window);

    glewExperimental = GL_TRUE;
    if (glewInit () != GLEW_OK) {
        printf ("Failed to initialize GLEW.\n");
        return -1;
    }

    int width, height;
    glfwGetFramebufferSize (window, &width, &height);
    glViewport (0, 0, width, height);

    /* Here comes the new code */

    // Define the vertex shader and compile it
    GLuint vertexShader = glCreateShader (GL_VERTEX_SHADER);
    glShaderSource (vertexShader, 1, &shaderSource, NULL);
    glCompileShader (vertexShader);

    // checking for errors
    GLuint success;
    GLchar infoLog[512]; // define a constant string to store errors informations
    glGetShaderiv (vertexShader, GL_COMPILE_STATUS, &success);
    
    if (!success) {
        glGetShaderInfoLog (vertexShader, 512, NULL, infoLog);
        printf ("Vertex shader compilation failed: %s\n", infoLog);
    }

    // create a fragment shader
    GLuint fragmentShader = glCreateShader (GL_FRAGMENT_SHADER);
    glShaderSource (fragmentShader, 1, &fragmentSource, NULL);
    glCompileShader (fragmentShader);

    glGetShaderiv (vertexShader, GL_COMPILE_STATUS, &success);

    if (!success) {
        glGetShaderInfoLog (fragmentShader, 512, NULL, infoLog);
        printf ("Fragment shader compilation failed: %s\n", infoLog);
    }

    //create shader program object and link to it the previous shaders
    GLuint shaderProgram;
    shaderProgram = glCreateProgram ();

    glAttachShader (shaderProgram, vertexShader);
    glAttachShader (shaderProgram, fragmentShader);
    glLinkProgram (shaderProgram);

    // test for linkage
    glGetProgramiv (shaderProgram, GL_LINK_STATUS, &success);
    if (!success) {
        glGetProgramInfoLog (shaderProgram, 512, NULL, infoLog);
        printf ("Failed to link the shaders to the shader program: %s", infoLog);
        
    }

    // everything went fine: creation of vertex and fragment shaders and their linkage
    // to the shader program object, now we use the program
    glUseProgram (shaderProgram);

    // we don't need the two shaders anymore
    glDeleteShader (vertexShader);
    glDeleteShader (fragmentShader);

    GLfloat vertices[] = {
        -0.5f, -0.5f, 0.0f,
        0.5f, -0.5f, 0.0f,
        0.0f,  0.5f, 0.0f
    };

    GLuint VBO, VAO, EBO;
    glGenVertexArrays (1, &VAO);
    glGenBuffers (1, &VBO);
    //glGenBuffers (1, &EBO);

    glBindVertexArray (VAO);
    glBindBuffer (GL_ARRAY_BUFFER, VBO);
    glBufferData (GL_ARRAY_BUFFER, sizeof (vertices), vertices, GL_STATIC_DRAW);


    glVertexAttribPointer (0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof (GLfloat), (GLvoid*)0);
    glEnableVertexAttribArray (0);
    
    // unbind buffers (setting them to 0)
    glBindBuffer (GL_ARRAY_BUFFER, 0);
    glBindVertexArray (0);

    while (!glfwWindowShouldClose (window)) {
        glfwPollEvents ();

        /* new code starts here */

        glClearColor (0.2f, 0.3f, 0.3f, 1.0f);
        glClear (GL_COLOR_BUFFER_BIT);

        glUseProgram (shaderProgram);
        glBindVertexArray (VAO);
        glDrawArrays (GL_TRIANGLES, 0, 3);
        glBindVertexArray (0);

        /* new code ends here */

        glfwSwapBuffers (window);
    }

    glfwTerminate ();
	return 0;
}
