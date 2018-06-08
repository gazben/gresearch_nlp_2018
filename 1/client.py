"""This is the main module"""
import webhandler
import querysolver
import rpnevaluator

def main():
    """Run client"""
    if not webhandler.API_KEY:
        raise ValueError("Set your API_KEY in webhandler.py! Find it on https://devrecruitmentchallenge.com/account")

    rpn_evaluator = rpnevaluator.RpnEvaluator()
    query_solver = querysolver.QuerySolver()

    print("Getting challenge list")
    challenge_list = webhandler.get_challenge_list()
    print("There are {} challenges".format(len(challenge_list)))

    for info in challenge_list:
        print("Solving challenge {} - {}".format(info.cid, info.challenge_type))
        challenge = webhandler.get_challenge(info.cid)

        if info.challenge_type == "rpn":
            handle_rpn(challenge, rpn_evaluator)
        elif info.challenge_type == "query":
            handle_query(challenge, query_solver)
        else:
            print("Unrecognised challenge type '{}'".format(info.challenge_type))

def handle_rpn(challenge, rpn_evaluator):
    """Handle an RPN challenge"""
    answers = {}
    for question in challenge.questions:
        try:
            answer = rpn_evaluator.evaluate_rpn(question.question)
            answers[question.tid] = answer
        except Exception as e:
            print(question.question)
            print(e)
            pass
    submission = {'challengeId': challenge.info.cid, 'answers': answers}
    result = webhandler.post_standard_submission(submission)
    print("Mark = {}%".format(result.mark))

def handle_query(challenge, solver):
    """Handle a general query challenge"""
    answers = {}
    for question in challenge.questions:
        answer = solver.answer_query(question.question)
        answers[question.tid] = answer
    submission = {'challengeId': challenge.info.cid, 'answers': answers}
    result = webhandler.post_standard_submission(submission)
    print("Mark = {}%".format(result.mark))


if __name__ == "__main__":
    main()
