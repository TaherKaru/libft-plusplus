# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abait-el <your@email.com>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/22 20:55:00 by abait-el          #+#    #+#              #
#    Updated: 2025/09/27 16:51:18 by abait-el         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ---------------------------------------------------------------------------- #
#                              Build Configuration                             #
# ---------------------------------------------------------------------------- #

NAME		=	libft.a

CC			=	cc
CFLAGS		=	-Wall -Wextra -Werror
AR			=	ar rcs
RM			=	rm -f

# ---------------------------------------------------------------------------- #
#                                   Colors                                     #
# ---------------------------------------------------------------------------- #

RED			=	\e[3;31m
GREEN		=	\e[3;32m
YELLOW		=	\e[3;33m
CYAN		=	\e[3;96m
END			=	\e[0m

SHELL := /bin/bash

# ---------------------------------------------------------------------------- #
#                                  Messages                                    #
# ---------------------------------------------------------------------------- #

OK			=	$(GREEN)[OK]$(END)
KO			=	$(RED)[KO]$(END)
INFO		=	$(CYAN)[INFO]$(END)
WARN		=	$(YELLOW)[WARN]$(END)

# ---------------------------------------------------------------------------- #
#                                 Sources                                      #
# ---------------------------------------------------------------------------- #

SRC_DIR = src
INCLUDE_DIR = include
OBJ_DIR = build/obj
LIB_DIR = build/lib
SRC			=	$(wildcard $(SRC_DIR)/*.c)
OBJ			=	$(patsubst $(SRC_DIR)/%.c, $(OBJ_DIR)/%.o, $(SRC))

# ---------------------------------------------------------------------------- #
#                                   Rules                                      #
# ---------------------------------------------------------------------------- #

all:		$(NAME)
	@echo -e "$(GREEN) libft.a has been successfuly built$(END)"

$(NAME):	 $(OBJ)
	@echo -e "$(CYAN) Object files has been built, Now creating libft.a...$(END)"
	@mkdir -p $(LIB_DIR)
	$(AR) $(LIB_DIR)/$(NAME) $(OBJ)

$(OBJ_DIR)/%.o:	$(SRC_DIR)/%.c
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) -I $(INCLUDE_DIR) -o $@ -c $<

clean:
	@$(RM) $(OBJ)
	@echo -e "$(WARN) Object files has been deleted."

fclean:		clean
	@$(RM) $(LIB_DIR)/$(NAME)
	@echo -e "$(WARN) $(NAME) has been deleted."

re: fclean all

.PHONY:		all clean fclean re bonus custom
