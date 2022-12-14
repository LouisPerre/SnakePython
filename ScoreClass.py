import os, csv, time, pygame, sys
from datetime import datetime


class Score:
    def write_score_file(self, score, time):
        # Write all the score in a csv file
        file_header = ['name', 'score', 'ingame_time', 'date']
        file_data = ['Player', score, time, (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")]
        headers = None
        if os.path.exists('./score.csv'):
            with open('score.csv', 'r', encoding='UTF8') as prepare_file:
                reader = csv.DictReader(prepare_file)
                headers = reader.fieldnames
        with open('score.csv', 'a', encoding='UTF8', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            if headers is not None:
                writer.writerow(file_data)
            else:
                writer.writerow(file_header)
                writer.writerow(file_data)

    def sortFn(self, dict):
        return dict['score']

    def draw_end_screen(self, snake, start_time, screen, apple, grid_size, grid_number, game_font, dead):
        # Draw the end screen with the current top score
        scores_list = []
        scoredStored = []
        score_x = int((grid_size * grid_number) / 2)
        score_y = int((grid_size * grid_number) / 2)
        if os.path.exists('./score.csv'):
            with open('score.csv', 'r', encoding='UTF8') as prepare_file:
                reader = csv.DictReader(prepare_file)
                for row in reader:
                    scores_list.append(row)
        scores_list.sort(key=self.sortFn, reverse=True)

        if len(scores_list) >= 3:
            scores_list = scores_list[0:3]

        if len(scores_list) >= 1:
            for score in scores_list:
                scoreStored_text = score['score'] + ' | ' + score['date'] + ' | ' + score['ingame_time'] + 's /  '
                scoreStored_surface = game_font.render(scoreStored_text, True, (56, 74, 12))
                scoreStored_rect = scoreStored_surface.get_rect(bottomright=(score_x, score_y - 90))
                scoredStored.append([scoreStored_surface, scoreStored_rect])

        highest_score = len(snake.body) - 3
        end_time = time.time()
        total_duration = end_time - start_time

        screen.fill((175, 215, 70))
        score_text = 'Your highest score is ' + str(highest_score)
        score_surface = game_font.render(score_text, True, (56, 74, 12))

        reload_text = 'To launch a new game press R'
        reload_surface = game_font.render(reload_text, True, (76, 74, 12))

        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midleft=(score_rect.right, score_rect.centery))
        reload_rect = reload_surface.get_rect(midtop=(score_x, score_y + 60))

        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        screen.blit(reload_surface, reload_rect)
        for index, scored in enumerate(scoredStored):
            if index == 0:
                screen.blit(scored[0], scored[1])
            elif index == 1:
                print(index - 1)
                screen.blit(scored[0], scored[0].get_rect(midleft=(scoredStored[index - 1][1].right, scoredStored[index - 1][1].centery)))
            elif index == 2:
                print(index - 1)
                screen.blit(scored[0], scored[0].get_rect(midtop=(scoredStored[index - 1][1].right, scoredStored[index - 1][1].centery + 30)))
        pygame.display.update()

        while dead:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.write_score_file(highest_score, round(total_duration))
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_r:
                        self.write_score_file(highest_score, round(total_duration))
                        snake.reset()
                        return False

