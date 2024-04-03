import argparse

from parser.parser import get_organization_reviews

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--org_id', type=str, required=True, help='''On the company page, the numbers in the address 
    bar.''')

    args = parser.parse_args()
    get_organization_reviews(org_id=args.org_id)
