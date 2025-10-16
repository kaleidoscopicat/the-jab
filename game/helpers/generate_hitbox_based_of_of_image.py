import pygame
from main import _hitbox_cache


def generate_hitbox(image, x, y):
    cache_key = (image.get_size(), id(image))

    if cache_key not in _hitbox_cache:
        if image.get_flags() & pygame.SRCALPHA == 0:
            temp = pygame.Surface(image.get_size(), pygame.SRCALPHA)
            temp.blit(image, (0, 0))
            image = temp

        mask = pygame.mask.from_surface(image)

        if mask.count() == 0:
            rect = image.get_rect()
            _hitbox_cache[cache_key] = rect
        else:
            bounds = mask.get_bounding_rects()
            if not bounds:
                rect = image.get_rect()
                _hitbox_cache[cache_key] = rect
            else:
                hitbox = bounds[0].unionall(bounds[1:]) if len(bounds) > 1 else bounds[0]
                _hitbox_cache[cache_key] = hitbox

    cached_rect = _hitbox_cache[cache_key].copy()
    cached_rect.x = x
    cached_rect.y = y
    return cached_rect
