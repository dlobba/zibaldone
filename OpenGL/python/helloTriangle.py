import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
import glfw

import numpy as np


shaderSource = """
    #version 330
    layout (location = 0) in vec3 position;
    void main ()
    {
        gl_Position = vec4 (position.x, position.y, position.z, 1.0);
    }"""

fragmentSource = """
    out vec4 color;
    void main ()
    {
        color = vec4 (1.0f, 0.5f, 0.2f, 1.0f);
    }"""

def main():
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Here comes the new code
    vertexShader = glCreateShader (GL_VERTEX_SHADER)
    glShaderSource (vertexShader, shaderSource)
    glCompileShader (vertexShader)

    success = 0
    infoLog = ""

    success = glGetShaderiv (vertexShader, GL_COMPILE_STATUS)

    if success != GL_TRUE:
        print ("Vertex shader compilation failed: " + str(glGetShaderInfoLog (vertexShader)))

    fragmentShader = glCreateShader (GL_FRAGMENT_SHADER)
    glShaderSource (fragmentShader, fragmentSource)
    glCompileShader (fragmentShader)

    success = 0
    infoLog = ""
    success = glGetShaderiv (fragmentShader, GL_COMPILE_STATUS)
    if not success:
        print ("Fragment shader compilation failed: " + str(glGetShaderInfoLog (fragmentShader)))

    shaderProgram = glCreateProgram ()
    glAttachShader (shaderProgram, vertexShader)
    glAttachShader (shaderProgram, fragmentShader)
    glLinkProgram (shaderProgram)

    # test for linkage
    success = glGetProgramiv (shaderProgram, GL_LINK_STATUS)
    if not success:
        print ("Failed to link the shaders to the shader program: " + str(glGetProgramInfoLog (shaderProgram)))

    glUseProgram (shaderProgram)
    glDeleteShader (vertexShader)
    glDeleteShader (fragmentShader)

    vertices = np.array(
        [-0.5, -0.5, 0.0,
         0.5, -0.5, 0.0,
         0.0, 0.5, 0.0],
        dtype = 'float32'
        )
    vertexDimension = 3
    nVertexed = 3
    
    VBO = VAO = EBO = None

    VAO = glGenVertexArrays (1)
    VBO = glGenBuffers (1)

    glBindVertexArray (VAO)
    glBindBuffer (GL_ARRAY_BUFFER, VBO)
    glBufferData (GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)
    glVertexAttribPointer (0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray (0)

    glBindBuffer (GL_ARRAY_BUFFER, 0)
    glBindVertexArray (0)
    
    # Loop until the user closes the window
    while not glfw.window_should_close(window):

        # Poll for and process events
        glfw.poll_events()


        # Render here, e.g. using pyOpenGL

        glClearColor (0.2, 0.3, 0.3, 1.0)
        glClear (GL_COLOR_BUFFER_BIT)
    
        glUseProgram (shaderProgram)
        glBindVertexArray (VAO)
        glDrawArrays (GL_TRIANGLES, 0, 3)
        glBindVertexArray (0)
        
        # Swap front and back buffers
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
