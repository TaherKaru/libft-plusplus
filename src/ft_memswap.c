/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memswap.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: abait-el <abait-el@example.com>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/27 16:48:14 by abait-el          #+#    #+#             */
/*   Updated: 2025/09/27 16:50:40 by abait-el         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_memswap(void *p1, void *p2, size_t typesize)
{
	unsigned char	tmp;
	size_t	i;

	i = 0;
	while (i < typesize)
	{
		tmp = *((unsigned char *)p1 + i);
		*((unsigned char *)p1 + i) = *((unsigned char *)p2 + i);
		*((unsigned char *)p2 + i) = tmp;
		i++;
	}
}
