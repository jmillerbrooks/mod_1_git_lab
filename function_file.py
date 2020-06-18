{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def read_all(namelist):\n",
    "    \"\"\"Read contents of zippedData into a named dictionary with names of\n",
    "    files as keys, dataframes as values.\n",
    "    \n",
    "    Takes a list of full filepaths.\n",
    "    \"\"\"\n",
    "    name_dict = {}\n",
    "    for filename in namelist:\n",
    "        #extract the portion of the filename corresponding to the \"name\"\n",
    "        name = filename[7:-7]\n",
    "        if filename.endswith('csv.gz'):\n",
    "            tmp_df = pd.read_csv(filename)\n",
    "            name_dict[name] = tmp_df\n",
    "        elif filename.endswith('tsv.gz'):\n",
    "        #both tsv are encoded in ascii per cmd line and chardet, but for some reason 'latin' appears to do the trick:\n",
    "            tmp_df = pd.read_csv(filename, sep='\\t', encoding='latin')\n",
    "            name_dict[name] = tmp_df\n",
    "        #in case there are any additional files in the dir\n",
    "        else:\n",
    "            continue\n",
    "    return name_dict"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
