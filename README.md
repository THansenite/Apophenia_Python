# Apophenia
Trying to find patterns in beer league chaos.

## Project Goals
1. (First Stage) A robust data mining engine for advanced analysis of game statistics
   * Player pairs (Frequent goal-assist combinations)
   * Referee Tendencies (common calls per ref, PM per game per ref, best/worst referee combinations)
   * Goalie nemesis
2. (Second Stage) A companion app for D League Radio broadcasters highlighting relevant information
   * When a player is entered in the system, automatically show relevant data (point milestones, when last goal was scored, etc.)
   * SportsEngine integration for automatic updates
   * Lots of input from broadcasters on helpful features
3. (Third Stage) Scouting report - Ability to take notes and get data on upcoming contests
   * Goal scorers and enablers (high assists)
   * Frequent penalties by certain players (if a player is likely to trip or get hot headed)
   * If a goalie tends to give up goals early, late, or in spurts
   * Ability to write private notes about a player's tendencies
   * Security of who can view

## Preliminary Task List
   * Get Season - Find the seasons list page for all seasons; differentiate between pre and post CIDL
   * Get Teams - For a season, find all the teams and different divisions
   * Get Schedule - For each season, get a list of all games
   * Get Game Data - Scrape data from game sheets?

## Stats to Track
   * Shots For/Against per team
   * Historic Player/Goalie stats
   * Historic Team Records
       * Team leaders
       * Championships/Runner-ups/Regular Season Championships won
       * Win/Loss streaks
   * Player History - Leagues, divisions, and teams played for
   * Players moving up/down divisions
   * Goalie records vs. individual teams
   * Team shots per period
   * Most shots in a single game
   * Goalie save percentage per period
   * Spider chart for players and goalies on key stats
   * Referee Stats - 
       * Liklihood of calling certain penalties
       * Dangerous combinations (ref pairs who call a lot of penalties)
       * Penalties against certain teams
   * Goalie nemesis
       * What player or team scores the most on a certain goalie
   * Player pick position vs. actual performance
   * Duration records
       * Team with longest duration of not trailing (1,4xx minutes for Knights)
       * Longest duration trailing while getting win (in a single game)
       * Goalie longest shutout streak
   * Consecutive games with a goal/assist/point
   * Milestones
       * 10/25/50/75/100 goals
       * 10/25/50/75/100 assists
       * 10/25/50/75/100 points
       * 5/10/15/20 shutouts
       * Should also do player who got to milestone fastest

   * Pre/Post CIDL Team History (need to work out how to handle this)
      * Rookies
      * Hat Tricks
      * Shutout streaks
      * Player/Team records
