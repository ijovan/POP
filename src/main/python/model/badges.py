from src.main.python.model.table import Table


class Badges(Table):
    TABLE_NAME = "badges"
    HEADER = [
        "id", "type", "award_count", "rank", "link", "name"
    ]

    def resolve_all(self):
        badges_users = \
            list(self.repository.badges_users.items.values())

        badges = []

        for badge_user in badges_users:
            badge = badge_user.copy()

            badge['id'] = badge.pop('badge_id')
            badge['type'] = badge.pop('badge_type')

            del badge['user_id']

            badges.append(badge)

        self.insert_list(badges)
