
def _BMR_FEMALE(age, weight_kg, height_cm):
    return (
        447.593 + (
            9.247 * weight_kg) + (
            3.098 * height_cm) - (
            4.330 * age)
    )

def _BMR_MALE(age, weight_kg, height_cm):
    return (
        88.362 + (
            13.397 * weight_kg) + (
            4.799 * height_cm) - (
            5.677 * age)
    )


