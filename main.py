import pygame

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame con Eventos")

# Definir eventos personalizados
ACCION_PERIODICA_EVENT = pygame.USEREVENT + 1
BUCLE_PRINCIPAL_EVENT = pygame.USEREVENT + 2

# Configurar temporizadores para los eventos personalizados
pygame.time.set_timer(ACCION_PERIODICA_EVENT, 5000)  # Cada 5 segundos
pygame.time.set_timer(BUCLE_PRINCIPAL_EVENT, 3000)   # Cada 3 segundos

# Función principal
def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == ACCION_PERIODICA_EVENT:
                print("Acción ejecutada.")
            elif event.type == BUCLE_PRINCIPAL_EVENT:
                print("La ejecución del loop principal continúa")

        # Clear the screen and update display
        screen.fill((0, 0, 0))
        pygame.display.flip()

        # Limitar el bucle principal a 60 frames por segundo
        clock.tick(60)

    pygame.quit()

# Ejecutar la función principal
main()
