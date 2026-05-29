def build_features(selected_movie, candidate_movie):

    return {
        "same_category": int(
            selected_movie["category"] ==
            candidate_movie["category"]
        ),

        "same_actor": int(
            selected_movie["actor"] ==
            candidate_movie["actor"]
        ),

        "same_age_rating": int(
            selected_movie["age_rating"] ==
            candidate_movie["age_rating"]
        )
    }