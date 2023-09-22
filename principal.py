import pygame
import math

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Triángulo Móvil")

# Colores
white = (255, 255, 255)

# Triángulo
triangle_color = (0, 0, 255)
triangle_half_width = 15  # Mitad del ancho del triángulo
triangle_half_length = 30  # Mitad de la longitud del triángulo
triangle_x = width // 2
triangle_y = height // 2
triangle_angle = 0
triangle_speed = 0
triangle_rotation_speed = 5
acceleration = 0.5  # Valor de aceleración
max_speed = 10  # Velocidad máxima
reverse_speed = 2  # Velocidad hacia atrás
deceleration = 0.05  # Valor de desaceleración

# Reloj
clock = pygame.time.Clock()

def wrap_around(x, y):
    # Asegura que las coordenadas x y y estén dentro de los límites de la pantalla
    if x < 0:
        x = width
    elif x > width:
        x = 0
    if y < 0:
        y = height
    elif y > height:
        y = 0
    return x, y

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Control de movimiento
    if keys[pygame.K_UP]:
        if triangle_speed < max_speed:
            triangle_speed += acceleration
    if keys[pygame.K_DOWN]:
        if triangle_speed > -reverse_speed:
            triangle_speed -= acceleration
    if keys[pygame.K_LEFT]:
        triangle_angle += triangle_rotation_speed
    if keys[pygame.K_RIGHT]:
        triangle_angle -= triangle_rotation_speed

    # Aplicar desaceleración constante
    if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        triangle_speed -= deceleration if triangle_speed > 0 else -deceleration if triangle_speed < 0 else 0

    # Mover el triángulo
    triangle_x += triangle_speed * math.cos(math.radians(triangle_angle))
    triangle_y -= triangle_speed * math.sin(math.radians(triangle_angle))
    triangle_x, triangle_y = wrap_around(triangle_x, triangle_y)

    # Limpiar la pantalla
    screen.fill(white)

    # Dibujar el triángulo
    points = [
        (
            triangle_x + triangle_half_length * math.cos(math.radians(angle)),
            triangle_y - triangle_half_width * math.sin(math.radians(angle)),
        )
        for angle in range(triangle_angle, triangle_angle + 360, 120)
    ]
    pygame.draw.polygon(screen, triangle_color, points)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la velocidad de fotogramas
    clock.tick(60)

# Salir de Pygame
pygame.quit()
